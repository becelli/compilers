from __future__ import annotations
from typing import Optional
from libraries.antlr.LALGParser import LALGParser
from libraries.antlr.LALGParserVisitor import LALGParserVisitor
from libraries.antlr.custom.LALGErrorListener import LALGErrorListener


class Symbol:
    def __init__(self: Symbol, name: str, type: str):
        self.name = name
        self.type = type


class Scope:
    def __init__(self, scope_name: str, enclosing_scope: Optional[Scope] = None):
        self.scope_name = scope_name
        self.enclosing_scope: Optional[Scope] = enclosing_scope
        self.symbols = {}

    def define(self, symbol: Symbol):
        self.symbols[symbol.name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        return self.symbols.get(name)


class LALGSemanticAnalyzer(LALGParserVisitor):
    def __init__(self, errorListener: LALGErrorListener):
        self.current_scope: Optional[Scope] = None
        self.errorListener = errorListener

    def enterScope(self, scope_name: str):
        scope = Scope(scope_name, self.current_scope)
        self.current_scope = scope

    def exitScope(self):
        self.current_scope = self.current_scope.enclosing_scope

    def visitProgram(self, ctx: LALGParser.ProgramContext):
        # Enter global scope
        self.enterScope("global")
        self.visitChildren(ctx)
        # Exit global scope
        self.exitScope()

    def visitProcedureDeclaration(self, ctx: LALGParser.ProcedureDeclarationContext):
        proc_name = ctx.IDENTIFIER().getText()
        if self.current_scope.resolve(proc_name):
            self.errorListener.semanticError(
                ctx.IDENTIFIER().symbol.line,
                ctx.IDENTIFIER().symbol.column,
                f"Procedure {proc_name} already declared",
            )
        else:
            # Define new procedure symbol in current scope
            symbol = Symbol(proc_name, "procedure")
            self.current_scope.define(symbol)
            # Enter new scope for the procedure body
            self.enterScope(proc_name)
            self.visitChildren(ctx)
            # Exit procedure scope
            self.exitScope()

    def visitVariableDeclaration(self, ctx: LALGParser.VariableDeclarationContext):
        var_type = ctx.type_().getText()
        for id_ctx in ctx.identifierList().IDENTIFIER():
            var_name = id_ctx.getText()
            if self.current_scope.resolve(var_name):
                self.errorListener.semanticError(
                    id_ctx.symbol.line,
                    id_ctx.symbol.column,
                    f"Variable {var_name} already declared in the {self.current_scope.scope_name} scope",
                )
            else:
                self.current_scope.define(Symbol(var_name, var_type))

    def visitAssignmentStatement(self, ctx: LALGParser.AssignmentStatementContext):
        var_name = ctx.variable().getText()
        var_symbol = self.current_scope.resolve(var_name)
        if var_symbol is None:
            self.errorListener.semanticError(
                ctx.variable().IDENTIFIER().symbol.line,
                ctx.variable().IDENTIFIER().symbol.column,
                f"Variable {var_name} not declared",
            )
            return

    def visitProcedureCallStatement(
        self, ctx: LALGParser.ProcedureCallStatementContext
    ):
        proc_name = ctx.IDENTIFIER().getText()
        proc_symbol = self.current_scope.resolve(proc_name)
        if proc_symbol is None:
            self.errorListener.semanticError(
                ctx.IDENTIFIER().symbol.line,
                ctx.IDENTIFIER().symbol.column,
                f"Procedure {proc_name} not declared",
            )
            return

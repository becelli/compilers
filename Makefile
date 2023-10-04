generate:
	java -jar libraries/antlr/antlr-4.13.1-complete.jar -Dlanguage=Python3 libraries/antlr/LALGLexer.g4 libraries/antlr/LALGParser.g4

execute:
	python3 project.py
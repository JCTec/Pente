import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="APente",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["AI.py", "Copy.py", "Deepcopy.py", "GameState.py", "move.py", "Node.py", "Pente.py", "Stack.py", "Pieces/blueGlassPiece.png", "Pieces/Cuadrado.png", "Pieces/fondo.jpg", "Pieces/greenGlassPiece.png", "Pieces/pente.png", "Pieces/penteBoard.png", "Pieces/undo.png", "Pieces/winner_blue.png", "Pieces/winner_green.png"]}},
    executables = executables

    )
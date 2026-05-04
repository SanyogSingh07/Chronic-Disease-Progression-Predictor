import typer
from src.cli import app as cli_app

main_app = typer.Typer(
    help="Disease Progression Prediction System",
    no_args_is_help=True
)

main_app.add_typer(cli_app)

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Welcome to the Disease Progression CLI!")
        print("1) Train Model")
        print("2) Predict Disease")
        
        choice = input("\nEnter your choice (1 or 2) [or press Enter for Help]: ").strip()
        if choice == "1":
            sys.argv.append("train")
        elif choice == "2":
            sys.argv.append("predict-disease")
            disease = input("Enter disease (e.g., diabetes): ").strip()
            sys.argv.append(disease)
            
    main_app()

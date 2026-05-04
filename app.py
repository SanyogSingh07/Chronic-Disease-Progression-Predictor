import sys
import os
from pathlib import Path

# Add project root to sys.path for robust imports
project_root = str(Path(__file__).parent.absolute())
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import typer
from rich.console import Console
from rich.panel import Panel
from src.cli import app as cli_app

console = Console()

main_app = typer.Typer(
    help="Chronic Disease Progression Prediction System",
    no_args_is_help=True
)

main_app.add_typer(cli_app)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        console.print(Panel.fit(
            "[bold blue]🏥 Chronic Disease Progression CLI[/bold blue]\n"
            "[italic]Professional Machine Learning Inference Tool[/italic]",
            border_style="green"
        ))
        print("\n1) Train Model")
        print("2) Predict Disease")
        
        choice = input("\nEnter your choice (1 or 2) [or press Enter for Help]: ").strip()
        if choice == "1":
            sys.argv.append("train")
        elif choice == "2":
            sys.argv.append("predict-disease")
            disease = input("Enter disease (e.g., diabetes): ").strip()
            sys.argv.append(disease)
            
    main_app()

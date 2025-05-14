import typer

from your_core_library.data_handler import get_core_greeting

app = typer.Typer(
    help="A simple CLI example that uses the project's core library.",
)


@app.command()
def main(
    name: str = typer.Option("World", help="The name to greet."),
    count: int = typer.Option(1, help="Number of times to print the core message."),
):
    """Say hello and demonstrate core library functionality."""
    greeting_msg = f"Hello {name}!"
    print(greeting_msg)

    for _ in range(count):
        core_msg = get_core_greeting(name)  # Use the imported function
        print(f"Core library says: {core_msg}")

    print(f"Printed the greeting {count} time(s) for {name}.")


if __name__ == "__main__":
    app()

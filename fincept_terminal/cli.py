import click
import logging
import warnings
import sys
import webbrowser
from fincept_terminal import update_checker
from fincept_terminal.display import display_art
from fincept_terminal.themes import console
from fincept_terminal.const import display_in_columns

# Suppress warnings and loggers
logging.getLogger('numexpr').setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

@click.group(invoke_without_command=True)
@click.version_option(version="0.1.3", prog_name="Fincept Investments Terminal")
@click.pass_context
def cli(ctx):
    """Fincept Investments CLI - Your professional financial terminal."""
    if ctx.invoked_subcommand is None:
        start()

# Start Command
@cli.command()
def start():
    """Start the Fincept Investments terminal."""
    # Check for updates on startup
    # show_image_splash_screen("C:\\Projects\\finceptTerminal\\finscript\\fincept.png")  # Path to your splash image
    # set_full_screen()  # Make the terminal full screen
    update_checker.check_for_update()

    # Display ASCII art and then the main menu
    display_art()
    show_main_menu()


import os
import platform

def set_full_screen():
    """Set the terminal window to full-screen mode."""
    if platform.system() == "Windows":
        os.system("mode con: cols=200 lines=50")  # Adjust dimensions
        os.system("powershell -command \"[System.Console]::WindowWidth = [System.Console]::LargestWindowWidth; [System.Console]::WindowHeight = [System.Console]::LargestWindowHeight\"")
    else:
        console.print("[bold yellow]Full-screen mode is not supported on this platform.[/bold yellow]")


from tkinter import Toplevel, Tk, Canvas
from PIL import Image, ImageTk
import time
import threading

def show_image_splash_screen(image_path):
    """Show a splash screen with an image."""
    def splash():
        root = Tk()
        root.overrideredirect(True)  # Remove window decorations (title bar, close button, etc.)
        root.geometry("600x400+400+200")  # Set window size and position

        # Display the image
        image = Image.open(image_path)
        image = image.resize((600, 400), Image.Resampling.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        photo = ImageTk.PhotoImage(image)

        canvas = Canvas(root, width=600, height=400)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, anchor="nw", image=photo)

        # Show the splash screen for a few seconds
        root.after(3000, root.destroy)  # Close after 3 seconds
        root.mainloop()

    # Run the splash screen in a separate thread
    splash_thread = threading.Thread(target=splash)
    splash_thread.start()
    splash_thread.join()  # Ensure it finishes before proceeding


def show_main_menu():
    """Main menu with navigation options."""
    console.print("\n")
    console.print("[bold cyan]MAIN MENU[/bold cyan]\n", style="info")

    main_menu_options = [
        "GLOBAL INDICES",  # 1
        "WORLD ECONOMY TRACKER",  # 2
        "GLOBAL NEWS & SENTIMENT",  # 3
        "GLOBAL STOCKS (EQUITIES)",  # 4
        "GLOBAL FUNDS",  # 5
        "EXCHANGE TRADED FUNDS",  # 6
        "GLOBAL BOND MARKET",  # 7 fixed income to add
        "OPTIONS & DERIVATIVES",  # 8
        "CRYPTOCURRENCY",  # 9
        "PORTFOLIO & INVESTMENT TOOLS",  # 10
        "GLOBAL STOCK SCANNER",  # 11
        "CURRENCY MARKETS (FOREX)",  # 12
        "COMMODITIES",  # 13
        "MONEY MARKET",  # 14
        "BACKTESTING STOCKS",  # 15
        "ROBO ADVISOR",  # 16
        "ADVANCE TECHNICALS",  # 17
        "GENAI QUERY",  # 18
        "FINSCRIPT",  # 19
        "EDUCATION & RESOURCES",  # 20
        "SETTINGS & CUSTOMIZATION",  # 21
        "TERMINAL DOCUMENTATION",  # 22
        "CONSUMER BEHAVIOUR",  # 23
        "LIVE PRICE INDIA",  # 24
        "SATELLITE IMAGERY ANALYSIS",  # 25
        "MARINE TRADE DATA",  # 26
        "INDIA MACRO & MICRO DATA",  # 27
        "EXIT",  # 28
        "FETCH LATEST NEWS",
        "ALPHA",
    ]

    # Display main menu in columns
    display_in_columns("Select an Option", main_menu_options)

    console.print("\n")
    from rich.prompt import Prompt
    choice = Prompt.ask("Enter your choice")

    try:
        choice = int(choice)  # Convert input to an integer
    except ValueError:
        console.print("[bold red]Invalid input. Please enter a valid option number.[/bold red]")
        return show_main_menu()  # Show the menu again on invalid input

    console.print("\n")

    # Call corresponding function based on the choice
    if choice == 1:
        from fincept_terminal.indices import show_global_indices_menu
        show_global_indices_menu()
    elif choice == 2:
        from fincept_terminal.economytracker import show_world_economy_tracker_menu
        show_world_economy_tracker_menu()
    elif choice == 3:
        from fincept_terminal.newsfetch import show_news_and_sentiment_menu
        show_news_and_sentiment_menu()
    elif choice == 4:
        from fincept_terminal.stock import show_equities_menu
        show_equities_menu()
    elif choice == 5:
        from fincept_terminal.funds import show_global_funds_menu
        show_global_funds_menu()
    elif choice == 6:
        from fincept_terminal.etfdata import show_etf_market_menu
        show_etf_market_menu()
    elif choice == 7:
        from fincept_terminal.bonds import show_bond_market_menu
        show_bond_market_menu()
    elif choice == 8:
        console.print("[bold red] Feature still in development [/bold red]", style="danger")
    elif choice == 9:
        from fincept_terminal.cryptodata import crypto_main_menu
        crypto_main_menu()
    elif choice == 10:
        from fincept_terminal.portfolio import show_portfolio_menu
        show_portfolio_menu()
    elif choice == 11:
        console.print("[bold red] Feature still in development [/bold red]", style="danger")
    elif choice == 12:
        from fincept_terminal.currencyforex import show_currency_market_menu
        show_currency_market_menu()
    elif choice == 13:
        console.print("[bold red] Feature still in development [/bold red]", style="danger")
    elif choice == 14:
        from fincept_terminal.moneymarket import show_money_market_menu
        show_money_market_menu()
    elif choice == 15:
        from fincept_terminal.portfolio import show_backtesting_menu
        show_backtesting_menu()
    elif choice == 16:
        from fincept_terminal.roboadvisor import show_robo_advisor_menu
        show_robo_advisor_menu()
    elif choice == 17:
        from fincept_terminal.advancetechnicals import show_technical_main_menu
        show_technical_main_menu()
    elif choice == 18:
        from fincept_terminal.GenAI import show_genai_query
        show_genai_query()
    elif choice == 19:
        from fincept_terminal.finscript import show_finscript_menu
        show_finscript_menu()
    elif choice == 20:
        console.print("[bold green]Under Construction...[/bold green]")
        show_main_menu()
    elif choice == 21:
        show_settings_menu()  # Call this function instead of calling a Click command
    elif choice == 22:
        webbrowser.open("https://docs.fincept.in")
        console.print("[bold green]Redirecting to Fincept Documentation...[/bold green]")
        show_main_menu()
    elif choice == 23:
        from fincept_terminal.consumer_behavior import show_consumer_behavior_menu
        show_consumer_behavior_menu()
    elif choice == 24:
        from fincept_terminal.liveprice import start_live_price_menu
        start_live_price_menu()
    elif choice == 25:
        from fincept_terminal.SatelliteImagery import show_car_analysis_menu
        show_car_analysis_menu()
    elif choice == 26:
        from fincept_terminal.marine import marine_menu
        marine_menu()
    elif choice == 27:
        from fincept_terminal.indiamacro import show_india_macro_micro_menu
        show_india_macro_micro_menu()
    elif choice == 28:
        console.print("[bold green]Exiting Fincept Terminal...[/bold green]")
        sys.exit(0)
    elif choice == 29:
        from fincept_terminal.newsfetcher import display_latest_news
        display_latest_news()
    elif choice == 30:
        from fincept_terminal.alphavantagee import display_stock_data
        display_stock_data()
    else:
        console.print("[bold red]Invalid option. Please select a valid menu option.[/bold red]")
        show_main_menu()  # Show the menu again if an invalid option is chosen

def show_settings_menu():
    """Settings menu with options displayed in a table."""
    while True:  # Use a loop to keep returning to the settings menu after each operation
        console.print("\n[bold cyan]SETTINGS MENU[/bold cyan]\n", style="info")

        settings_options = [
            "Change Theme",  # 1
            "Configure Display Options",  # 2
            "Toggle Notifications",  # 3
            "Toggle Auto-Update",  # 4
            "Display Current Configurations",  # 5
            "Back to Main Menu",  # 6
        ]

        # Display settings options in columns
        display_in_columns("Settings Options", settings_options)

        console.print("\n")
        from rich.prompt import Prompt
        choice = Prompt.ask("Enter your choice")

        try:
            choice = int(choice)  # Convert input to an integer
        except ValueError:
            console.print("[bold red]Invalid input. Please enter a valid option number.[/bold red]")
            continue  # Show the settings menu again on invalid input

        console.print("\n")

        # Handle settings menu choices
        if choice == 1:
            from fincept_terminal.settings import change_theme
            change_theme()
        elif choice == 2:
            from fincept_terminal.settings import configure_display
            configure_display()
        elif choice == 3:
            from fincept_terminal.settings import toggle_notifications
            toggle_notifications()
        elif choice == 4:
            from fincept_terminal.settings import toggle_auto_update
            toggle_auto_update()
        elif choice == 5:
            display_current_configurations()
        elif choice == 6:
            show_main_menu()  # Go back to the main menu
            break
        else:
            console.print("[bold red]Invalid option. Please select a valid menu option.[/bold red]")


def display_current_configurations():
    """Fetch and display the current user configurations."""
    from fincept_terminal.settings import load_settings

    # Load the current settings from the settings file
    settings = load_settings()

    # Create a table to display settings in a structured way
    from rich.table import Table
    table = Table(title="Current Configurations", title_justify="center", header_style="bold cyan")

    table.add_column("Setting", style="bold yellow", justify="left")
    table.add_column("Value", style="bold white", justify="left")

    # Add settings and their values to the table
    table.add_row("Theme", settings.get("theme", "Not set"))
    table.add_row("Display Rows", str(settings.get("display_rows", "Not set")))
    table.add_row("Notifications", "Enabled" if settings.get("notifications", False) else "Disabled")
    table.add_row("Auto-Update", "Enabled" if settings.get("auto_update", False) else "Disabled")

    # Display the table
    console.print(table)



if __name__ == '__main__':
    from fincept_terminal.utils import load_environment
    load_environment()
    cli()

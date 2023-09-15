from trade_analysis import cli
import typer

def main():
    typer.run(cli.main)
    
if __name__ == '__main__':
    main()
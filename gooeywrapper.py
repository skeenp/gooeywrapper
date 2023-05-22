import sys
from enum import Enum
import argparse

class GooeyMode(Enum):
    GUI_CLI = 'gui_cli'
    CLI = 'cli'
    GUI = 'gui'


class GooeyWrapper:
    """
    A wrapper class for managing the execution mode (GUI, CLI, or GUI+CLI) and argument parsing using Gooey and argparse.

    Args:
        main_func (callable): The main function to be executed.

    Attributes:
        app_mode (GooeyMode): The current execution mode.
        main_func (callable): The main function to be executed.
        parser (argparse.ArgumentParser or GooeyParser): The argument parser.

    """
    
    argument_parser = None  
    
    def __init__(self, main_func: callable):
        self.app_mode = GooeyMode.CLI
        self.main_func = main_func

        # Detect the execution mode
        if '--ignore-gooey' in sys.argv:
            sys.argv.remove('--ignore-gooey')
            self.app_mode = GooeyMode.GUI_CLI
        elif len(sys.argv) == 1:
            self.app_mode = GooeyMode.GUI
        else:
            self.app_mode = GooeyMode.CLI

    def run(self, **gooey_args: dict):
        """
        Run the application based on the detected execution mode.

        Args:
            gooey_args (dict): Additional arguments for Gooey (applicable only in GUI mode).

        """
        # Setup parsers based on the execution mode
        if self.app_mode in [GooeyMode.GUI_CLI, GooeyMode.CLI]:
            self.argument_parser = argparse.ArgumentParser()
            self.main_func(wrapper=self)
        else:
            from gooey import Gooey, GooeyParser
            self.argument_parser = GooeyParser()
            Gooey(self.main_func, **gooey_args)(self)

    @property
    def mode(self) -> GooeyMode:
        """
        Get the current execution mode.

        Returns:
            GooeyMode: The current execution mode.

        """
        return self.app_mode

    def add_argument(self, parent, *args: list, **kwargs: dict):
        """
        Add an argument to the argument parser based on the execution mode.

        Args:
            *args (list): Positional arguments for adding an argument to the parser.
            **kwargs (dict): Keyword arguments for adding an argument to the parser.

        """
        if self.app_mode != GooeyMode.GUI:
            kwargs.pop('widget', None)
            kwargs.pop('gooey_options', None)

        # Add the argument to the parser
        self.parser.add_argument(*args, **kwargs)

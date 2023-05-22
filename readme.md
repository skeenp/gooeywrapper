# Gooey Wrapper

The `gooeywrapper` library is a Python wrapper that simplifies the management of execution modes (GUI, CLI, or GUI+CLI) and argument parsing using the Gooey and argparse libraries. It provides a convenient way to create command-line applications with optional graphical user interfaces (GUIs) using the awesome [Gooey library](https://github.com/chriskiehl/Gooey).

## Features

- **Execution Mode Detection:** The `gooeywrapper` automatically detects the execution mode based on command-line arguments. It supports three modes: GUI, CLI, and GUI+CLI.
- **Argument Parsing:** The library seamlessly integrates with the argparse module to handle argument parsing in both CLI and GUI modes. It allows you to define command-line arguments and their respective options in a unified manner.
- **Gooey Integration:** In GUI and GUI+CLI modes, the library uses the Gooey library to generate a graphical user interface for the application. It provides a wide range of GUI widgets and options to enhance the user experience.

## Installation

You can install the `gooeywrapper` library using pip:

```
git clone https://github.com/your-username/gooey_wrapper.git
```

## Usage

Here's an example of how to use the `gooeywrapper` library in your Python script:

```python
import argparse
from gooeywrapper import GooeyWrapper, GooeyMode

def main(wrapper: GooeyWrapper):
    # Add arguments based on the execution mode
    # Parse command-line arguments
    parser = wrapper.argument_parser(
        description='My Application',
        epilog='This is the end of the application.'
    )
    # Using the wrapper, add an arguement
    wrapper.add_argument(parser, 'input', help='Input file path')
    # The add argument function can also be used to add an argument to a subparser or group
    subparser = parser.add_subparsers(help='sub-commands help')
    wrapper.add_argument(subparser, 'output', help='Output file path')
    wrapper.add_argument(subparser, '--verbose', help='Enable verbose mode', action='store_true')

    args = parser.parse_args()

    # Add instance-specific code
    if wrapper.mode == GooeyMode.CLI:
        print('Running in the command line!')
    elif wrapper.mode == GooeyMode.GUI_CLI:
        print('Running in GUI+CLI mode!')
    elif wrapper.mode == GooeyMode.GUI:
        print('Running in GUI mode!')

if __name__ == "__main__":
    # Create a GooeyWrapper instance, passing the main function
    gooeywrapper = GooeyWrapper(main)
    # Run the application
    gooeywrapper.run()
```

The wrapper passes itself to the main function so that the parser, add_argument, and mode elements can be accessed within the main script. In this way, you can tailor the ArgumentParser object to your personal project.

## Contributing

Contributions to the `gooeywrapper` library are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your forked repository.
4. Submit a pull request describing your changes.

## Issues
If you encounter any issues with the gooeywrapper library, please open an issue on the GitHub repository and provide detailed information about the problem.

## Contact
For any questions or inquiries, you can reach out to the project maintainer at maintainer@example.com.

## License
This library is released under the MIT License. See the LICENSE file for more details.

I hope you find the gooeywrapper library helpful in simplifying the development of your command-line applications with optional GUIs. If you have any further questions or need assistance, feel free to ask!

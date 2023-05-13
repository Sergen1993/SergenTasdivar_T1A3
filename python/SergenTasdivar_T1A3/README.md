# Sneaker Shop Terminal App

This is a simple terminal application that allows users to view and purchase sneakers. Users can view the available products, add them to the cart, view the cart, and proceed to checkout. The application is built using Python and utilizes various programming concepts and packages.

## Installation

To install the application, follow these steps:

1. Clone the repository: `git clone <https://github.com/Sergen1993/SergenTasdivar_T1A3.git>`
2. Change into the project directory: `cd SergenTadivar_T1A3`
3. Install the required packages: `pip install tabulate termcolor`

## Dependencies

The application requires the following Python packages:

- `tabulate`: Used to format the product gallery and cart table.
- `termcolor`: Used to add color to the terminal output.

## System Requirements

The application has the following system requirements:

- Python 3.6 or higher installed
- Terminal or command prompt

## Usage

To run the application, navigate to the project directory and execute the following command: `python3 sneaker_app.py`


## Features

The application includes the following features:

1. **View Products**: Allows users to view the available sneakers and their prices.
2. **Add Product to Cart**: Enables users to add a selected product to their cart.
3. **View Cart**: Displays the items in the cart, along with their prices and quantities.
4. **Checkout**: Allows users to proceed with the purchase and complete the checkout process.

## Implementation Plan

The following is the implementation plan for each feature:

1. View Products:
   - Retrieve the product data from the `products.py` file.
   - Format and display the product gallery table using the `tabulate` package.
   - Implement error handling for invalid inputs.

2. Add Product to Cart:
   - Prompt the user to select a product from the product gallery.
   - Ask for the desired quantity of the selected product.
   - Add the selected product and quantity to the cart.
   - Display a success message upon adding to the cart.
   - Implement error handling for invalid inputs.

3. View Cart:
   - Format and display the cart table using the `tabulate` package.
   - Calculate and display the total price.
   - Implement error handling for an empty cart.

4. Checkout:
   - Display the cart items and total price.
   - Prompt the user to confirm the checkout.
   - If confirmed, display a thank you message and exit the application.
   - If not confirmed, cancel the checkout and return to the main menu.

The implementation plan will be tracked using a project management platform called trello
![Trello board checklist](/images/t1a3_R7.png)

 https://trello.com/invite/b/FKnqSZ0Z/ATTI1b133a953da8ecbfb119feb695cf51ecEDAB8650/game-development-template



## Code Style

The code follows the PEP 8 style guide for Python. It adheres to the recommended coding conventions and style practices to ensure consistency and readability.

## Help Documentation

To use and install the application, follow these instructions:

1. Installation:
   - Clone the repository: `git clone <https://github.com/Sergen1993/SergenTasdivar_T1A3.git>`
   - Change into the project directory: `cd SergenTasdivar_T1A3`
   - Install the required packages: `pip install tabulate termcolor`

2. Dependencies:
   - The application requires the following Python packages: `tabulate` and `termcolor`.
   - Install the dependencies using the provided installation instructions.

3. System Requirements:
   - Ensure that Python 3.6 or higher is installed on your system.
   - Use a terminal or command prompt to run the application.

4. Command Line Usage:
   - Navigate to the project directory.
   - Run the application using the command: `python sneaker_app.py`

## Source Control

The source code for this
application is hosted on a source control repository. You can access the repository at [GitHub](https://github.com/Sergen1993/SergenTasdivar_T1A3.git).

## Tests

The application includes the following tests:

1. **View Products Test**:
   - Test Case 1: User selects "View Products" from the menu.
     - Expected Result: The product gallery is displayed correctly.
   - Test Case 2: User selects "View Products" with no products available.
     - Expected Result: An appropriate message is displayed indicating no products are available.

2. **Add to Cart Test**:
   - Test Case 1: User selects "Add Product to Cart" and provides valid inputs.
     - Expected Result: The product is added to the cart successfully.
   - Test Case 2: User selects "Add Product to Cart" and provides invalid inputs.
     - Expected Result: An error message is displayed, and the user is prompted to enter valid inputs.

These tests cover important features of the application and verify that it is running as expected.

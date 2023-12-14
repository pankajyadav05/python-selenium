### Take-Home Assignment: Selenium WebDriver Testing with Python and Reporting

## Objective

Develop an automated test suite using Selenium WebDriver in Python to perform geolocation testing and login, register functionality testing. [BONUS] Generate JSON reports for each test case.

## Tasks

1. **Geolocation Testing Using Selenium with Chrome DevTools**:

   - Implement tests using Selenium for Python for geolocation emulation [Use this site](https://my-location.org).
   - Include tests for specific geolocation scenarios, utilizing Selenium's DevTools integration.

2. **Login Functionality Testing on LambdaTest Ecommerce(dummy website for Web Automation Testing)**:

   - Automate the login process for the [LambdaTest Ecommerce](https://ecommerce-playground.lambdatest.io/index.php?route=account/login).
   - Test both successful login and handling of invalid credentials.

3. **Python Environment Setup**:

   - Set up a Python virtual environment for your project.
   - Use `requirements.txt` for managing dependencies like Selenium, Chrome WebDriver, and any other libraries.
   - Instructions on setting up and activating the virtual environment should be included in the documentation.

4. **Documentation**:

   - Provide a `README.md` file with instructions on how to:
     - Set up the Python environment and install dependencies.
     - Run the tests.
     - View the test reports (if JSON reporting is implemented).

5. **Submission**:
   - Submit the project URL as a PRIVATE Git repository to prithvi@smartdino.tech and cc arun@smartdino.tech..
   - **Give repo access to the pankajyadav.code@gmail.com**
   - Ensure code quality and organization are in line with best practices.

## Bonus

- **JSON Report Generation**: Utilize Python testing frameworks like `pytest` with plugins like `pytest-json` or `pytest-html` for report generation.

## Evaluation Criteria

- **Code Quality**: Clean, well-organized, maintainable code.
- **Test Coverage**: Comprehensive tests covering the specified scenarios.
- **Python Environment Setup**: Proper use of virtual environments and dependency management.
- **Reporting**: Accurate and informative JSON or HTML reports for each test.
- **Documentation**: Clear, concise instructions in the `README.md`.
- **If you're not able to implement all parts of the task, partial submissions are welcome.**
- Check full details about Evaluation criteria here [MARKS.md](MARKS.md)

## Example Commands for README.md

- **To Install Dependencies**:

  ```bash
  pip install -r requirements.txt
  ```

- **To Run Tests**:

  ```bash
  pytest
  ```

- **Viewing Reports**:
  Provide instructions on where to find the generated reports after test execution.

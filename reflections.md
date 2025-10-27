Q1 ANS : 
Easiest error to fix were the unused import error and the "use of eval" error because the lines throwing these errors just had to be removed
Hardest error to fix was the Name Styling error as it was the most tedious as I had to convert all the function names from Camel Case to snake_case and had to add docstrings.

Q2 ANS:
Based on the errors shown, the tools did not show any false positives


Q3 ANS: 
I would integrate them at both the local and remote stages of development, as suggested in the lab handout.I would use IDE/editor plugins for tools like Flake8 and Pylint to get instant, real-time feedback as I write code. I would configure a CI pipeline (like GitHub Actions) to automatically run pylint, bandit, and flake8 against the entire project every time a new pull request is opened.

Q4 ANS:
Applying the six fixes from the table tangibly improved the code's quality, readability, and robustness. The code is now more robust because I fixed the Mutable default arg bug (preventing shared logs) and replaced the Bare 'except' to only catch specific KeyErrors, which stops it from hiding all other bugs. The most critical improvement was to security, where removing the Use of eval line eliminated a major vulnerability. Finally, readability and maintainability improved by using the with statement for safer file handling, renaming functions to snake_case for standard Python convention, and removing the unused import to reduce clutter.


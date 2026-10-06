 ### 6 oct 
 project setup. uv commands to initialise project


-  uv init
-  uv add pygame
-  uv python pin 3.12
-  uv add pygame
-  uv add --dev pytest
-  uv sync
-  uv run pytest

PyGame isn't available on 3.14
`uv run pytest` runs my tests
uv helps me run the code on other computers

git setup and first save

- git init
- git add .python-version README.md project-diary.md pyproject.toml pytest.toml src uv.lock tests
- git status
- git commit -m 'setup for project'
- git config --global --edit
- git commit --amend --reset-author
- gitk --all &

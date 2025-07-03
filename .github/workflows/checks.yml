name: checks

on:
  push:
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Install uv
      run:
        curl -LsSf https://astral.sh/uv/install.sh | sh
    - name: Check http(s) links
      run:
        uv run scripts/check_links.py

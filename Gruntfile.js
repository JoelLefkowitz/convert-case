const { merge } = require("lodash");
const { simple } = require("quick-grunt");

const tasks = [
  {
    name: "lint",
    description: "Lint the source code.",
    exec: ["cspell", "pylint", "autoflake", "mypy", "remark"],
  },
  {
    name: "format",
    description: "Format the source code.",
    exec: ["black", "isort", "prettier", "alphabetize"],
  },
  {
    name: "test",
    description: "Compile and run unit tests.",
    clean: ["tests"],
    exec: ["tox"],
  },
  {
    name: "build",
    description: "Build source distributions for publishing.",
    clean: ["build"],
    exec: ["distributions"],
  },
];

const clean = {
  build: ["build", "dist"],
  tests: ["coverage"],
};

const copy = {};

const flakeOptions = `
   -v -ri --exclude 'venv, conftest.py'
   --remove-unused-variables
   --remove-all-unused-imports
   --ignore-init-module-imports
`;

const linters = {
  autoflake: `autoflake . ${flakeOptions}`,
  cspell: 'npx cspell ".*" "*" "**/*"',
  missing: "conductor cspell words",
  mypy: "mypy . --exclude 'venv'",
  pylint: "pylint --rcfile .pylintrc  --fail-under=8 src tests",
  remark: "npx remark -r .remarkrc --ignore-path .gitignore . .github",
};

const formatters = {
  alphabetize: "conductor cspell format",
  black: "black .",
  isort: "isort .",
  prettier: "npx prettier . --write --ignore-path .gitignore",
};

const setuptools = {
  distributions: "python setup.py sdist bdist_wheel",
};

const tests = {
  tox: "tox . -e py",
};

const docs = {
  quickdocs: "quickdocs .quickdocs.yml",
};

const exec = merge(linters, formatters, setuptools, tests, docs);

module.exports = simple({ clean, copy, exec }, tasks);

const flakeOptions = `
   -v -ri --exclude 'venv, conftest.py'
   --remove-unused-variables
   --remove-all-unused-imports
   --ignore-init-module-imports
`;

const tools = {
  autoflake: `autoflake . ${flakeOptions}`,
  black: 'black .',
  cspell: 'npx cspell ".*" "*" "**/*"',
  isort: 'isort .',
  mypy: `mypy . --exclude '(src/core|venv)'`,
  prettier: 'npx prettier . --write --ignore-path .gitignore --single-quote',
  pylint: 'pylint --rcfile .pylintrc  --fail-under=8 src tests',
  remark: 'npx remark -r .remarkrc --ignore-path .gitignore . .github',
  tox: 'tox . -e py',
};

const kvs = (arr) => Object.fromEntries(arr.map((i) => [i, i]));

const comprehension = (obj, cb) =>
  Object.fromEntries(Object.entries(obj).map(cb));

const commands = (arr) =>
  arr.reduce((acc, x) => acc.concat(x.includes(':') ? x : 'exec:'.concat(x)), [
    'clean',
  ]);

module.exports = (grunt) => {
  grunt.initConfig({
    clean: kvs(['coverage']),
    exec: comprehension(tools, ([k, v]) => [k, { cmd: v, stdout: 'inherit' }]),
  });

  grunt.loadNpmTasks('grunt-exec');
  grunt.loadNpmTasks('grunt-contrib-clean');

  grunt.registerTask(
    'lint',
    'Lint the source code.',
    commands(['cspell', 'pylint', 'mypy', 'remark'])
  );

  grunt.registerTask(
    'format',
    'Format the source code.',
    commands(['black', 'isort', 'autoflake', 'prettier'])
  );

  grunt.registerTask(
    'test',
    'Sequentially run all unit test suites',
    commands(['tox'])
  );
};

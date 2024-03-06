# Terra social network

## How to run a project

3. Open a terminal in the root directory of the project
4. Run <code>docker-compose up -d --build</code>
5. Now you can visit website at <a>localhost:8080</a> and API docs at <a>localhost:5000/docs</a>

## How to run API tests

1. Open terminal in the root directory of the project
2. Run <code>docker-compose -f docker-compose.test.yml up --exit-code-from backend</code>

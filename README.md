# Terra social network

## How to run a project

1. Open _services/backend_ folder
2. Create an <code>.env.dev</code> file similar to <code>.env.example</code>
3. Open a terminal in the root directory of the project
4. Run <code>docker-compose up -d --build</code>
5. Now you can visit website at <a>localhost:8080</a> and API docs at <a>localhost:5000/docs</a>

## How to run API tests

1. Open _services/backend_ folder
2. Create an <code>.env.test</code> file with the test database credentials, similar to <code>.env.example</code>
3. Create a virtual environment and install the packages
3. Open a terminal here and run <code>pytest -v</code>

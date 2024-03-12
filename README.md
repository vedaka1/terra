# Terra social network

## How to run a project
Create a <code>.env</code> file in the <code>services/backend</code> directory like a <code>.env.example</code>

### For production

1. Open the terminal in the root directory of the project
2. Run <code>docker-compose -f docker-compose.deploy.yml up -d</code>
3. Now you can visit website at <a>localhost:8080</a> and API docs at <a>localhost:5000/docs</a>

### For development

1. Open the terminal in the root directory of the project
2. Run <code>docker-compose up -d --build</code>
3. Now you can visit website at <a>localhost:8080</a> and API docs at <a>localhost:5000/docs</a>

## How to run API tests

1. Create a test database <code>docker run --name test-db -e POSTGRES_DB=terra -e POSTGRES_USER=username -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:15.1</code>
3. Open the terminal in the folder <code>services/backend</code>
4. Install requirements <code>pip install -r requirements.txt</code>
4. Run <code>pytest -v</code>

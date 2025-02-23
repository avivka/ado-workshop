# My Python Microservices App

This project is a sample application demonstrating a basic microservices architecture using Python and Flask. It consists of two services, `service1` and `service2`, which communicate with each other and can be run in a containerized environment using Docker.

## Project Structure

```
python-ms-app
├── service1
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── service2
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── common
│   ├── __init__.py
│   └── utilities.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone [<repository-url>](https://github.com/avivka/ado-workshop.git)
   cd python-ms-app
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. For each service, install the specific dependencies:
   ```
   cd service1
   pip install -r requirements.txt
   cd ../service2
   pip install -r requirements.txt
   ```

4. To run the services using Docker, ensure you have Docker installed and run:
   ```
   docker-compose up
   ```

## Usage

- Access `service1` at `http://localhost:5000`
- Access `service2` at `http://localhost:5001`

## Contributing

Feel free to submit issues or pull requests for improvements or additional features.

## License

This project is licensed under the MIT License.
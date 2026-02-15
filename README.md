Inventory Management System (Flask + REST API)

A full-stack inventory management solution featuring a Flask REST API, a Command Line Interface (CLI), and an Interactive Web Dashboard. This system integrates with the OpenFoodFacts API to automatically enrich product data (like brands and ingredients) based on product names.


//FEATURES
Interactive Web UI: Manage your inventory visually through index.html with real-time updates.
Full CRUD API: Create, Read, Update, and Delete inventory items.
External API Integration: Automatically fetches product details from OpenFoodFacts.
Dual Interface: Choose between the modern Web Dashboard or the functional Terminal CLI.
Automated Testing: Comprehensive test suite using pytest


//INSTALLATION & SETUP

1. Clone the repository:
```
cd inventory_lab
```

2. Install dependencies:
```
pip install flask requests pytest
```

3. Project Structure:
```
├── app.py              # Flask Server & Routes
├── inventory.py        # In-memory Data Logic
├── external_api.py     # OpenFoodFacts API Logic
├── cli.py              # Command Line Interface
├── templates/
│   └── index.html      # Web Dashboard (Frontend)
└── tests/              # Pytest Suite
```


//HOW TO RUN

1. Start the Backend Server
```
python app.py
```
The server will start at http://127.0.0.1:5000.

2.Access the Web Interface
Once the server is running, open your browser and navigate to:
```
http://127.0.0.1:5000
```
This will load the index.html file stored in the templates folder. From here, you can:
View the current inventory in a table.
Add new items using the form (which automatically fetches data from OpenFoodFacts).
Update price and stock levels directly in the table.
Delete items with a single click.

3. Use the CLI Tool
If you prefer the terminal, open a separate window and run:
```
python cli.py
```

4. Run Unit Tests
To validate the logic across all layers:
```
pytest
```
Or
```
python3 -m pytest
```


import sqlite3

def init_db():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the pokemon table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        image TEXT NOT NULL
    )
    ''')

    # Read Pokemon data from file
    pokemon_data = []
    try:
        with open('pokemon.txt', 'r') as file:
            for line in file:
                # Split the line by pipe character and strip whitespace
                parts = [part.strip() for part in line.split('|')]
                if len(parts) == 3:  # Ensure we have all required fields
                    pokemon_id = int(parts[0])
                    # Construct the PokeAPI sprite URL
                    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
                    pokemon_data.append((
                        pokemon_id,  # id
                        parts[1],    # name
                        parts[2],    # description
                        image_url    # image URL
                    ))
    except FileNotFoundError:
        print("Error: pokemon.txt file not found!")
        return
    except Exception as e:
        print(f"Error reading pokemon.txt: {e}")
        return

    # Insert the data
    cursor.executemany('''
    INSERT OR REPLACE INTO pokemon (id, name, description, image)
    VALUES (?, ?, ?, ?)
    ''', pokemon_data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print(f"Database initialized successfully with {len(pokemon_data)} Pokemon entries!")

if __name__ == '__main__':
    init_db() 
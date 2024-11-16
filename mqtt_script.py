import paho.mqtt.client as mqtt
import psycopg2

# Function to connect to PostgreSQL database
conn = psycopg2.connect(database="formqtt",
                        host="dpg-csrd9gl6l47c73fcrehg-a.oregon-postgres.render.com",
                        user="formqtt_user",
                        password="JczzxkQ8NIHwCfWesX0Kb1a3OkwiRuaF",
                        port="5432")

cursor = conn.cursor()

def on_message(client, userdata, msg):
    # Extract message data
    topic = msg.topic
    payload = msg.payload.decode()
    
    # Insert message data into PostgreSQL database
    cursor.execute("INSERT INTO mqtt_messages (topic, message) VALUES (%s, %s)", (topic, payload))
    conn.commit()

# MQTT setup
client = mqtt.Client()
client.on_message = on_message

client.username_pw_set("Azdex609", "Salsa609")

client.connect("35.212.240.173", 1883)
client.subscribe("#")  # Subscribe to all topics or specify your topics

client.loop_forever()
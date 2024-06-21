import psycopg2

conn = psycopg2.connect(
  host = "localhost",
  database = "fliperama",
  user = "postgres",
  password = "admin",
  port = "5432"
)
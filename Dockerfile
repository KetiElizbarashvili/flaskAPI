# Use the official PostgreSQL image
FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgrespw
ENV POSTGRES_DB=postgres

# Expose the PostgreSQL port
EXPOSE 5432
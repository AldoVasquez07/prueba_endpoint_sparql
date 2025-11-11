from flask import Flask, request, jsonify
from rdflib import Graph

app = Flask(__name__)

# Cargar datos RDF (puedes usar un archivo .ttl o .rdf)
g = Graph()
g.parse("datos.ttl", format="turtle")

@app.route("/sparql", methods=["GET", "POST"])
def sparql_endpoint():
    query = request.args.get("query") or request.form.get("query")
    if not query:
        return "Falta el parámetro 'query'", 400

    try:
        results = g.query(query)
        data = [dict(row) for row in results.bindings]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5000)

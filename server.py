import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

# Tentukan direktori root untuk server web, di sini kita menggunakan folder 'static'
Handler.directory = "static"

# Membuat dan menjalankan server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()

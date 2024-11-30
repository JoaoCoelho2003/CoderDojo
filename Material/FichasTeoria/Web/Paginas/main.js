const http = require('http');
const fs = require('fs');
const path = require('path');

// Set up the port for the server
const port = 3000;

// MIME type helper function
const getMimeType = (ext) => {
    switch (ext) {
        case '.jpg':
        case '.jpeg':
            return 'image/jpeg';
        case '.png':
            return 'image/png';
        case '.mp4':
            return 'video/mp4';
        case '.ico':
            return 'image/x-icon';
        default:
            return 'application/octet-stream';
    }
};

// Create HTTP server
const server = http.createServer((req, res) => {
    // Serve the HTML page
    if (req.url === '/') {
        fs.readFile(path.join(__dirname, 'tagsPrincipais.html'), (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('500 - Internal Server Error');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    }
    // Serve images
    else if (req.url.startsWith('/imagens')) {
        const imagePath = path.join(__dirname, req.url);
        fs.readFile(imagePath, (err, data) => {
            if (err) {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('404 - Not Found');
            } else {
                const ext = path.extname(imagePath);
                const contentType = getMimeType(ext);
                res.writeHead(200, { 'Content-Type': contentType });
                res.end(data);
            }
        });
    }
    // Serve videos
    else if (req.url.startsWith('/videos')) {
        const videoPath = path.join(__dirname, req.url);
        fs.readFile(videoPath, (err, data) => {
            if (err) {
                res.writeHead(404, { 'Content-Type': 'text/plain' });
                res.end('404 - Not Found');
            } else {
                const ext = path.extname(videoPath);
                const contentType = getMimeType(ext);
                res.writeHead(200, { 'Content-Type': contentType });
                res.end(data);
            }
        });
    }
    else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 - Not Found');
    }
});

// Start the server
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});

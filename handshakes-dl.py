import logging
import json
import os
import glob

import pwnagotchi
import pwnagotchi.plugins as plugins

from flask import abort, send_from_directory, render_template_string, request, jsonify

TEMPLATE = """
{% extends "base.html" %}
{% set active_page = "handshakes" %}

{% block title %}
    {{ title }}
{% endblock %}

{% block styles %}
    {{ super() }}
    <style>
        #filter {
            width: 100%;
            font-size: 16px;
            padding: 12px 20px 12px 40px;
            border: 1px solid #ddd;
            margin-bottom: 12px;
        }
        .handshake-item {
            position: relative;
        }
        .handshake-item .details {
            display: none;
            position: absolute;
            top: 20px;
            left: 100px;
            background-color: white;
            border: 1px solid #ddd;
            padding: 10px;
            z-index: 1;
        }
    </style>
{% endblock %}

{% block script %}
    var shakeList = document.getElementById('list');
    var filter = document.getElementById('filter');
    var filterVal = filter.value.toUpperCase();

    filter.onkeyup = function() {
        document.body.style.cursor = 'progress';
        var table, tr, tds, td, i, txtValue;
        filterVal = filter.value.toUpperCase();
        li = shakeList.getElementsByTagName("li");
        for (i = 0; i < li.length; i++) {
            txtValue = li[i].textContent || li[i].innerText;
            if (txtValue.toUpperCase().indexOf(filterVal) > -1) {
                li[i].style.display = "list-item";
            } else {
                li[i].style.display = "none";
            }
        }
        document.body.style.cursor = 'default';
    }

    function deleteHandshake(filename) {
        if (confirm('Are you sure you want to delete ' + filename + '?')) {
            fetch('/plugins/handshakes-dl/delete/' + filename, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById(filename).remove();
                } else {
                    alert('Error deleting file');
                }
            });
        }
    }

    function showDetails(filename) {
        fetch('/plugins/handshakes-dl/details/' + filename)
        .then(response => response.json())
        .then(data => {
            var detailsDiv = document.getElementById('details-' + filename);
            detailsDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
            detailsDiv.style.display = 'block';
        });
    }
{% endblock %}

{% block content %}
    <input type="text" id="filter" placeholder="Search for ..." title="Type in a filter">
    <ul id="list" data-role="listview" style="list-style-type:disc;">
        {% for handshake in handshakes %}
            <li class="file handshake-item" id="{{handshake}}">
                <a href="/plugins/handshakes-dl/{{handshake}}">{{handshake}}</a>
                <button onclick="deleteHandshake('{{handshake}}')">Delete</button>
                <button onclick="showDetails('{{handshake}}')">Details</button>
                <div class="details" id="details-{{handshake}}"></div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
"""

class HandshakesDL(plugins.Plugin):
    __author__ = 'me@sayakb.com'
    __version__ = '0.3.0'
    __license__ = 'GPL3'
    __description__ = 'Download handshake captures from web-ui.'

    def __init__(self):
        self.ready = False

    def on_loaded(self):
        logging.info("[HandshakesDL] plugin loaded")

    def on_config_changed(self, config):
        self.config = config
        self.ready = True

    def on_webhook(self, path, request):
        if not self.ready:
            return "Plugin not ready"

        if path == "/" or not path:
            handshakes = glob.glob(os.path.join(self.config['bettercap']['handshakes'], "*.pcap"))
            handshakes = [os.path.basename(path)[:-5] for path in handshakes]
            return render_template_string(TEMPLATE,
                                          title="Handshakes | " + pwnagotchi.name(),
                                          handshakes=handshakes)

        elif path.startswith("delete/"):
            filename = path[len("delete/"):]
            file_path = os.path.join(self.config['bettercap']['handshakes'], filename + '.pcap')
            try:
                os.remove(file_path)
                return jsonify({"success": True})
            except FileNotFoundError:
                return jsonify({"success": False, "error": "File not found"})
            except Exception as e:
                return jsonify({"success": False, "error": str(e)})

        elif path.startswith("details/"):
            filename = path[len("details/"):]
            file_path = os.path.join(self.config['bettercap']['handshakes'], filename + '.pcap')
            try:
                # Replace this with actual file details extraction logic
                details = {
                    "size": os.path.getsize(file_path),
                    "created": os.path.getctime(file_path),
                    "modified": os.path.getmtime(file_path)
                }
                return jsonify(details)
            except FileNotFoundError:
                return jsonify({"error": "File not found"})
            except Exception as e:
                return jsonify({"error": str(e)})

        else:
            dir = self.config['bettercap']['handshakes']
            try:
                logging.info(f"[HandshakesDL] serving {dir}/{path}.pcap")
                return send_from_directory(directory=dir, filename=path+'.pcap', as_attachment=True)
            except FileNotFoundError:
                abort(404)

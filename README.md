# Weather Around Me

This project is a simple home weather utility that uses the **Gdańskie Wody rain measurement API** to fetch and analyze local rainfall data.  
The goal is to build a lightweight, local “weather hub” that will later run on a **Raspberry Pi**.

## Purpose

The application retrieves rainfall data from:

https://pomiary.gdanskiewody.pl/home/rain

It uses **FastAPI** to structure and analyze incoming requests, allowing more detailed inspection of the measurement data.

## Technologies Used

- **FastAPI** – backend framework for request handling and analysis  
- **Python** – main programming language  
- **Gdańskie Wody API** – source of real rainfall measurements  
- **Raspberry Pi (planned)** – future deployment target for local hosting  

## Project Goal

The goal of this project is to create a small, local weather service that:

- Fetches rainfall data from Gdańskie Wody  
- Processes and analyzes the measurements  
- Runs as a FastAPI microservice  
- Eventually operates on a Raspberry Pi as a home weather station  

## Current State

The project is currently in development. The main focus is:

- Connecting to the Gdańskie Wody rain API  
- Structuring the backend using FastAPI  
- Preparing the logic for future Raspberry Pi deployment  

## Summary

This is a personal project aimed at building a local rain‑monitoring service using **FastAPI** and the **Gdańskie Wody** measurement API, with plans to host it on a **Raspberry Pi** for everyday home use.

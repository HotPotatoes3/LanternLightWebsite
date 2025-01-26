# Lantern Light Broadcast

Welcome to the Lantern Light Broadcast website! This project is the digital home of our student-run radio broadcast show for the students of UC Merced. Visit us at [llbroadcast.org](http://llbroadcast.org) to check out our latest updates and broadcasts.

---

## Description
Lantern Light Broadcast is a hub for our student community to come together and enjoy a mix of entertainment, news, and discussion through our live and recorded broadcasts. The website features:

- **Latest Broadcast:** An embedded YouTube player displaying the most recent broadcast from our channel.
- **Social Media Links:** Quick access to our YouTube and Discord for community interaction and updates.
- **Development in Progress:** The website is still under active development with more features to come.

---

## Features
- Landing page with a clean, responsive design based on the [Helios HTML5 template](https://html5up.net/helios) (free for personal and commercial use).
- Links to our YouTube and Discord communities.
- Embedded YouTube player showcasing the latest broadcast.

---

## Installation

Follow these steps to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HotPotatoes3/LanternLightWebsite.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd lantern-light-broadcast
   ```

3. **Set up your environment:**
   - Install Python (3.8 or higher recommended).
   - Install `pip`, if not already installed.


4. **Set up environment variables:** (For youtube api mainly rn)
   - Create a `.env` file in the root directory.
   - Add the required environment variables (e.g., API keys, configuration values). Example:
     ```env
     SECRET_KEY=your_secret_key
     API_KEY=your_api_key
     ```

5. **Run the development server:**
   ```bash
   python app.py
   ```

6. **Access the website:**
   Open your browser and go to `http://127.0.0.1:5000`.

---

## Usage
This project uses the Flask framework. Key dependencies include:

```python
from flask import Flask, request, render_template, abort
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
```

The website is designed to be lightweight and scalable, allowing for future additions and improvements as the community grows.

---

## Contributing
Contributions are welcome! Here’s how you can get involved:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a detailed commit message"
   ```
4. Push your changes:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License
This project incorporates the [Helios HTML5 template](https://html5up.net/helios), which is free to use for personal or commercial purposes. All custom code and content are licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [HTML5 UP](https://html5up.net/) for the Helios template.
- UC Merced students for their ongoing support.
- Our amazing community on YouTube and Discord.

---

Thank you for checking out Lantern Light Broadcast! Stay tuned for exciting updates and broadcasts!


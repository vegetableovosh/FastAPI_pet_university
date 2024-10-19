
---
alembic init migrations
---

---
alembic revision --autogenerate -m "comment"
---

---
alembic upgrade heads
---

---
pip install "fastapi[all]"
---

---
python3 -m pip install -r requirements.txt
---

---
sudo apt-get install libpq-dev python3-dev
---

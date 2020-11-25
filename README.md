# Separate auth Blueprint (done)

Serve auth blueprint under /auth/ url prefix
```python
app.register_blueprint(auth_bp, url_prefix='/auth')
```
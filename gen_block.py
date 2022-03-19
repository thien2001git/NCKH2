f = open("tx.txt","w", encoding="utf-8")
x = "static 'css/main.css'"
f.write("{% static 'css/main.css' %} {% endblock %}")
f.close()
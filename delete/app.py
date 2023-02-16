
@app.route("/delete/<string:id>")
#Login required kısmı ise - kullanıcının girmesini yasaklama veya bu işlemi yap daha sonra gir olarak ayarlayabilirsiniz. Bu işlemi nasıl yapabilirsiniz.
# Bu işlemi Flask Decorator yardımı ile yapabilirsiinz.
@login_required
def delete(id):
    cursor = mysql.connection.cursor()
    i = "Select * From makale where author = %s and id = %s "

    c = cursor.execute(i,(session["username"],id))

    if c>0:
        sorgu2 = "Delete from makale where id = %s"
        
        cursor.execute(sorgu2,(id,))
        mysql.connection.commit()
        return redirect(url_for("kontrol"))
        
    else:
        flash("Bu makale silinemedi.","danger")
        return redirect(url_for("index"))


#Tek bir işlem ile silmek isterseniz basit bir kod satırıyla bu işlemi tamamlayabilirsiniz.

@app.route("/delete/<string:id>")
def silmek(id):
    cursor = mysql.connection.cursor()
    i = "Delete from makale where id = %s"
    cursor.execute(i,(id,))
    mysql.connection.commit()
    cursor.close()
    flash("Başarıyla silindi.","success")
    return redirect(url_for("kontrol"))

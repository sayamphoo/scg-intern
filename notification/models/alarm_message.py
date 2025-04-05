from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def rz_alert(actual, limit=13.4, machine="", product=""):
    return f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; border-radius: 8px;">
            <h2 style="text-align: center;">🚨⚠️ Rz ALERT!! ⚠️🚨</h2>
            <p>💥 <strong>ค่า Rz สูงเกินกำหนด!</strong> 💥</p>
            <p>
                <strong>📊 Actual:</strong> {actual} <br>
                <strong>📏 Limit:</strong> {limit}
            </p>
            <p>
                <strong>🛠️ Machine:</strong> {machine} <br>
                <strong>📦 Product:</strong> {product}
            </p>
            <p>
                <strong>🕒 Datetime:</strong> {get_timestamp()}
            </p>
           <br>
            <p style="font-weight: bold;">
                ‼️ กรุณาตรวจสอบด่วน ก่อนเกิดความเสียหาย ‼️
            </p>
            <hr>
        </div>
    """

def wz_alert(actual, limit=1.4, machine="", product=""):
    return f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; border-radius: 8px;">
            <h2 style="text-align: center;">🚨⚠️ Wz ALERT!! ⚠️🚨</h2>
            <p>⚡ <strong>ค่า Wz ทะลุเพดาน!</strong> ⚡</p>
            <p>
                <strong>📊 Actual:</strong> {actual} <br>
                <strong>📏 Limit:</strong> {limit}
            </p>
            <p>
                <strong>🛠️ Machine:</strong> {machine} <br>
                <strong>📦 Product:</strong> {product}
            </p>
            <p>
                <strong>🕒 Datetime:</strong> {get_timestamp()}
            </p>
            <br>
            <p style="font-weight: bold;">
                🛑 หยุดเครื่องและตรวจสอบโดยด่วน!
            </p>
            <hr>
        </div>
    """

def us_alert(actual, limit, machine="", product=""):
    return f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; border-radius: 8px;">
            <h2 style="text-align: center;">🚨📉 US UNDER LIMIT!! 📉🚨</h2>
            <p>❗ <strong>ค่า US ต่ำกว่าที่กำหนด</strong> ❗</p>
            <p>
                <strong>📊 Actual:</strong> {actual} <br>
                <strong>📏 Limit:</strong> {limit}
            </p>
            <p>
                <strong>🛠️ Machine:</strong> {machine} <br>
                <strong>📦 Product:</strong> {product}
            </p>
            <p>
                <strong>🕒 Datetime:</strong> {get_timestamp()}
            </p>
            <br>
            <p style="font-weight: bold;">
                ⚠️ อาจส่งผลต่อคุณภาพชิ้นงาน!
            </p>
            <hr>
        </div>
    """

def is_alert(actual, limit, machine="", product=""):
    return f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; border-radius: 8px;">
            <h2 style="text-align: center;">🚨📉 IS UNDER LIMIT!! 📉🚨</h2>
            <p>❗ <strong>ค่า IS ต่ำเกินไป</strong> ❗</p>
            <p>
                <strong>📊 Actual:</strong> {actual} <br>
                <strong>📏 Limit:</strong> {limit}
            </p>
            <p>
                <strong>🛠️ Machine:</strong> {machine} <br>
                <strong>📦 Product:</strong> {product}
            </p>
            <p>
                <strong>🕒 Datetime:</strong> {get_timestamp()}
            </p>
            <br>
            <p style="font-weight: bold;">
                ⚠️ โปรดตรวจสอบระบบการผลิต!
            </p>
            <hr>
        </div>
    """

def dimension_alert(width, length, thickness, width_limit, length_limit, thickness_limit, machine="", product=""):
    return f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; border-radius: 8px;">
            <h2 style="text-align: center;">🚨📏 DIMENSION ALERT!! 📏🚨</h2>
            <p>❌ <strong>ขนาดไม่ตรงตามสเปค</strong> ❌</p>
            <p>
                <strong>🔹 Width:</strong> {width} (Limit = {width_limit[0]} - {width_limit[1]}) <br>
                <strong>🔹 Length:</strong> {length} (Limit = {length_limit[0]} - {length_limit[1]}) <br>
                <strong>🔹 Thickness:</strong> {thickness} (Limit = {thickness_limit[0]} - {thickness_limit[1]})
            </p>
            <p>
                <strong>🛠️ Machine:</strong> {machine} <br>
                <strong>📦 Product:</strong> {product}
            </p>
            <p>
                <strong>🕒 Datetime:</strong> {get_timestamp()}
            </p>
            <br>
            <p style="font-weight: bold;">
                🔥 อย่าละเลย! ความผิดพลาดนี้อาจกระทบทั้งล็อต!
            </p>
            <hr>
        </div>
    """

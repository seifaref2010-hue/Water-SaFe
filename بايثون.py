# نسخة Console-based للكود، تشتغل على أي جهاز ثقيل أو على Thonny بدون Tkinter أو Streamlit

# === دوال التحليل ===
def calculate_pollution(data):
    score = 0
    if data.get('color') in ['بنية', 'رمادية', 'صفراء']:
        score += 20
    if data.get('impurities') in ['رمل', 'جزيئات صغيرة', 'شوائب واضحة']:
        score += 30
    if data.get('pipe_age') in ['5–10 سنوات', 'أكثر من 10 سنوات']:
        score += 15
    return score

def water_quality(pollution):
    return 100 - pollution

def water_status(quality):
    if quality >= 80:
        return '🟢 صالحة للشرب'
    elif quality >= 50:
        return '🟡 صالحة للاستخدام فقط'
    else:
        return '🔴 غير صالحة'

def suggested_solution(data):
    solutions = []
    if data.get('impurities') in ['رمل', 'جزيئات صغيرة', 'شوائب واضحة']:
        solutions.append('فلتر رواسب')
    if data.get('smell') in ['كلور']:
        solutions.append('فلتر كربون')
    if data.get('taste') in ['مر', 'ملح']:
        solutions.append('فلتر 3 مراحل')
    return ', '.join(solutions) if solutions else 'لا حاجة لفلتر'

# === واجهة Console ===
def main():
    print('=== لوحة تحكم جودة المياه ===')
    username = input('اسم المستخدم: ').strip()
    password = input('كلمة المرور: ').strip()

    if not username or not password:
        print('خطأ: الرجاء إدخال اسم المستخدم وكلمة المرور')
        return

    print(f'مرحباً {username}! أدخل بيانات المياه التالية:')

    # جمع البيانات
    data = {}
    data['color'] = input('لون المياه (شفافة/صفراء/بنية/رمادية/غير واضح): ').strip()
    data['smell'] = input('رائحة المياه (لا توجد/كلور/صدأ/كبريت/غريبة): ').strip()
    data['taste'] = input('طعم المياه (طبيعي/معدني/ملح/مر/غير معروف): ').strip()
    data['shape'] = input('شكل المياه (شفافة/عكارة خفيفة/عكارة شديدة): ').strip()
    data['impurities'] = input('شوائب (لا يوجد/رمل/جزيئات صغيرة/شوائب واضحة): ').strip()
    data['pipe_age'] = input('عمر المواسير (أقل من 5 سنوات/5–10 سنوات/أكثر من 10 سنوات/غير معروف): ').strip()
    data['pipe_type'] = input('نوع المواسير (بلاستيك/حديد/نحاس/غير معروف): ').strip()
    data['tank'] = input('خزان مياه (نعم/لا): ').strip()
    data['last_clean'] = input('آخر تنظيف (أقل من 6 أشهر/سنة/أكثر من سنة/لا أعرف): ').strip()
    data['pressure'] = input('ضغط المياه (ضعيف/متوسط/قوي): ').strip()
    data['color_change'] = input('تغير اللون (نعم/لا/لا أعرف): ').strip()
    data['always_problem'] = input('مشكلة دائمة (نعم/أحيانًا): ').strip()

    # تحليل البيانات
    pollution = calculate_pollution(data)
    quality = water_quality(pollution)
    status = water_status(quality)
    solution = suggested_solution(data)

    # عرض النتائج
    print('\n=== نتائج التحليل ===')
    print(f'درجة جودة المياه: {quality}')
    print(f'نسبة التلوث: {pollution}%')
    print(f'الحالة: {status}')
    print(f'الحل المقترح: {solution}')

if __name__ == '__main__':
    main()

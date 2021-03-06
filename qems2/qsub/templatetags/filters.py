from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
from qems2.qsub.models import *
from qems2.qsub.utils import sanitize_html, strip_markup

@register.filter(name='lookup')
def lookup(dict, key):
    if key in dict:
        return dict[key]
    else:
        return 0
    
@register.filter(name='tossup_or_bonus')
def tossup_or_bonus(type):
    return str(type)

@register.filter(name='tossups_or_bonuses')
def tossups_or_bonuses(type):
    if type == 'tossup':
        return 'tossups'
    if type == 'bonus':
        return 'bonuses'
    return type

@register.filter(name='get_editor_categories')
def get_editor_categories(editor, tour):
    
    if Role.objects.filter(player=editor, tournament=tour).exists():
        role = Role.objects.get(player=editor, tournament=tour)
        categories = role.category.split(';')
    
        cat_list = [cat_tuple[1] for cat_tuple in CATEGORIES if cat_tuple[0] in categories]
    else:
        cat_list = []
    
    return mark_safe('<p>' + '<br>'.join(cat_list) + '</p>')

@register.filter(name='preview')
def preview(text):
    return mark_safe(text[0:81] + '...')

@register.filter(name='bonus_answers')
def bonus_answers(bonus):
    return mark_safe('<p>' + bonus.part1_answer[0:80].encode('utf-8') + '</p><p>'
    + bonus.part2_answer[0:80].encode('utf-8') + '</p><p>'
    + bonus.part3_answer[0:80].encode('utf-8') + '</p>')

@register.filter(name='percent')
def percent(x, y):
    try:
        if float(y) != 0:
            return '{0:0.2f}'.format(100 * float(x) / float(y))
        else:
            return None
    except Exception as ex:
        return None

@register.filter(name='check_mark_if_100_pct')
def check_mark_if_100_pct(x, y):
    percentage = percent(x, y)
    if percentage == '100.00' or percentage == None:
        return mark_safe('<i class="fa fa-check" style="color:green"></i>')
    else:
        return mark_safe('<i class="fa fa-times" style="color:red"></i>')
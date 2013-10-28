# coding=utf-8

import difflib
import re
import traceback
from poll.models import Poll, STARTSWITH_PATTERN_TEMPLATE
from eav.models import Attribute

def find_best_response(session, poll):
    resps = session.responses.filter(response__poll=poll, response__has_errors=False).order_by('-response__date')
    if resps.count():
        resp = resps[0].response
        typedef = Poll.TYPE_CHOICES[poll.type]
        if typedef['db_type'] == Attribute.TYPE_TEXT:
            return resp.eav.poll_text_value
        elif typedef['db_type'] == Attribute.TYPE_FLOAT:
            return resp.eav.poll_number_value
        elif typedef['db_type'] == Attribute.TYPE_OBJECT:
            return resp.eav.poll_location_value
    return None

def find_closest_match(value, model, match_exact=False):
    try:
        name_str = value.lower().encode('utf-8')
        toret = None

        model_names = model.values_list('name', flat=True)
        model_names_lower = [ai.lower().encode('utf-8') for ai in model_names]
        model_names_matches = difflib.get_close_matches(name_str, model_names_lower)

        if model_names_matches:
            toret = model.get(name__iexact=model_names_matches[0])
            return toret
    except Exception, exc:
            print traceback.format_exc(exc)
            return None

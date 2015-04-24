from xml.dom.minidom import parse, parseString

dom = parse('from.xml')

def find_child_nodes(node, name):
    result = []
    for child_node in node.childNodes:
        if child_node.nodeName == name:
            result.append(child_node)
    return result

def find_first_node(node, name):
    child_nodes = find_child_nodes(node, name)
    if not child_nodes:
        return None
    return child_nodes[0]

def get_node_value(node):
    try:
        return node.childNodes[0].nodeValue
    except:
        return None

root_node = dom.childNodes[0]
for calendar_items in find_child_nodes(root_node, 'calendar-items'):
    for exercise in find_child_nodes(calendar_items, 'exercise'):
        created_node = find_first_node(exercise, 'created')
        created = get_node_value(created_node)
        print created
        # TODO: Time
        # TODO: Sport

        result_node = find_first_node(exercise, 'result')

        # TODO: distance
        # TODO: calories
        # TODO: duration

        zones_node = find_first_node(result_node, 'zones')

        zones_nodes = find_child_nodes(zones_node, 'zone')
        for zone_node in zones_nodes:
            upper_node = find_first_node(zone_node, 'upper')
            print get_node_value(upper_node)
            lower_node = find_first_node(zone_node, 'lower')
            print get_node_value(lower_node)
            in_zone_node = find_first_node(zone_node, 'in-zone')
            print get_node_value(in_zone_node)

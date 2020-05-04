from api import models


def process_disk_info(host_object, disk_dict):
    """
    处理汇报来的硬盘信息
    :return:
    """
    if not disk_dict['status']:
        print('硬盘资产信息没有获取到')
        print('获取硬盘资产时出错：',disk_dict['error'])
        return

    new_disk_dict = disk_dict['data']
    new_disk_slot_set = set(new_disk_dict)

    db_disk_queryset = models.Disk.objects.filter(server=host_object).all()
    db_disk_dict = {row.slot:row for row in db_disk_queryset}
    db_disk_slot_set = set(db_disk_dict)

    create_slot_set = new_disk_slot_set - db_disk_slot_set
    remove_slot_set = db_disk_slot_set - new_disk_slot_set
    update_slot_set = new_disk_slot_set & db_disk_slot_set

    record_str_list = []

    # 添加
    for slot in create_slot_set:
        models.Disk.objects.create(**new_disk_dict[slot],server=host_object)
        msg = r"【新增硬盘】槽位：{slot}，类型：{pd_type}，容量{capacity}".format(**new_disk_dict[slot])
        record_str_list.append(msg)
    # 删除
    models.Disk.objects.filter(server=host_object,slot__in=remove_slot_set).delete()
    if remove_slot_set:
        msg = "【删除硬盘】槽位：{}".format(','.join(remove_slot_set))
        record_str_list.append(msg)

    # 更新
    for slot in update_slot_set:
        temp = []
        for key,value in new_disk_dict[slot].items():
            old_value = getattr(db_disk_dict[slot],key)
            if value == old_value:
                continue
            msg = "硬盘的{}，由{}变更成了{}".format(key,old_value,value)
            temp.append(msg)
            setattr(db_disk_dict[slot],key,value)
        if temp:
            db_disk_dict[slot].save()
            row = "【更新硬盘】槽位：{},更新的内容：{}".format(slot,';'.join(temp))
            record_str_list.append(row)

    if record_str_list:
        models.AssetsRecord.objects.create(content="\n".join(record_str_list),server=host_object)
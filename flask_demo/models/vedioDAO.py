import gridfs


class VedioDAO(object):

    def __init__(self, database):
        self.db = database
        self.videos = self.db.vedio_list

    def save_video(self, vedio_obj, vedio_name):
        grid = gridfs.GridFS(self.db, "videos")
        _id = grid.put(vedio_obj)
        vedio_obj.close()

        self.videos.insert({'grid_id': _id, 'name': vedio_name})

    def get_vedio(self, name):

        doc = self.videos.find_one({'name': name})
        if doc is None:
            return False




from extract import *
from vector import *
import os

def matchs(image_path, db, t_compare, use_cs, controller):
        # Melakukan matching dan menghasilkan 3 gambar teratas yang paling "mirip"
        if use_cs:
            controller.score_name = 'Similarity'
        else:
            controller.score_name = 'Distance'
        if image_path is not None:
            controller.hide_buttons()
            controller.msg.set('Extracting %s...' %image_path.split('/')[-1])
            controller.matched_images = []
            dsc = extractFeatures(image_path)
            for compared_path in db:
                controller.msg.set('\rMatching: %s' %compared_path)
                compared_data = dict()
                compared_data['path'] = compared_path
                compared_image = db[compared_path]
                if use_cs:
                    compared_data['x'] = calcCosineSimilarity(dsc, compared_image)
                else:
                    compared_data['x'] = calcEuclideanDistance(dsc, compared_image)
                controller.matched_images.append(compared_data)
                if use_cs:
                    controller.matched_images = sorted(controller.matched_images, key = lambda x: -x['x'])
                else:
                    controller.matched_images = sorted(controller.matched_images, key = lambda x: x['x']) 
                if len(controller.matched_images) > t_compare:
                    controller.matched_images = controller.matched_images[0:t_compare]
        
            controller.show_buttons()
            controller.draw_matches()
            controller.msg.set('Match with: ' + controller.matched_images[0]['path'] + ' (' + str(controller.matched_images[0]['x']) + ') ')
        else:
            controller.msg.set('Open a file first.')


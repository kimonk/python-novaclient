# Copyright 2010 Jacob Kaplan-Moss
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Image interface.
"""

from six.moves.urllib import parse

from novaclient import base


class Bitstream(base.Resource):
    """
    An bitstream is a collection of files used to create or rebuild a server.
    """
    HUMAN_ID = True

    def __repr__(self):
        return "<Bitstream: %s>" % self.name

    def delete(self):
        """
        Delete this bitstream.
        """
        self.manager.delete(self)


class BitstreamManager(base.ManagerWithFind):
    """
    Manage :class:`Bitstream` resources.
    """
    resource_class = Bitstream

    def get(self, image):
        """
        Get an Bitstream.

        :param image: The ID of the Bitstream to get.
        :rtype: :class:`Bitstream`
        """
        return self._get("/bitstreams/%s" % base.getid(image), "image")

    def list(self, detailed=True, limit=None, marker=None):
        """
        Get a list of all images.

        :rtype: list of :class:`Image`
        :param limit: maximum number of images to return.
        :param marker: Begin returning images that appear later in the image
                       list than that represented by this image id (optional).
        """
        params = {}
        detail = ''
        if detailed:
            detail = '/detail'
        if limit:
            params['limit'] = int(limit)
        if marker:
            params['marker'] = str(marker)
        params = sorted(params.items(), key=lambda x: x[0])
        query = '?%s' % parse.urlencode(params) if params else ''

        return self._list('/bitstreams%s%s' % (detail, query), 'images')

    def delete(self, image):
        """
        Delete an image.

        It should go without saying that you can't delete an image
        that you didn't create.

        :param image: The :class:`Image` (or its ID) to delete.
        """
        self._delete("/bitstreams/%s" % base.getid(image))

    def set_meta(self, image, metadata):
        """
        Set an images metadata

        :param image: The :class:`Image` to add metadata to
        :param metadata: A dict of metadata to add to the image
        """
        body = {'metadata': metadata}
        return self._create("/bitstreams/%s/metadata" % base.getid(image),
                            body, "metadata")

    def delete_meta(self, image, keys):
        """
        Delete metadata from an image

        :param image: The :class:`Image` to delete metadata
        :param keys: A list of metadata keys to delete from the image
        """
        for k in keys:
            self._delete("/bitstreams/%s/metadata/%s" % (base.getid(image), k))

import api from "./api.ts"

export const propertiesApi = {
  async getAll() {
    const res = await api.get("/properties");
    return res.data;
  },

  async getById(id: number) {
    const res = await api.get(`/properties/${id}`);
    return res.data;
  },

  async create(data: unknown) {
    const res = await api.post("/properties", data);
    return res.data;
  },

  async update(id: number, data: unknown) {
    const res = await api.put(`/properties/${id}`, data);
    return res.data;
  },

  async delete(id: number) {
    const res = await api.delete(`/properties/${id}`);
    return res.data;
  },

  // PHOTOS

  async getPhotos(propertyId: number) {
    const res = await api.get(`/properties/${propertyId}/photos`);
    return res.data;
  },

  async deletePhoto(photoId: number) {
    const res = await api.delete(`/properties/photos/${photoId}`);
    return res.data;
  },
};

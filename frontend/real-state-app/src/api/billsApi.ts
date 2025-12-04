import api from "./api";

export const billsApi = {
  async getAll() {
    const res = await api.get("/property-bills");
    return res.data;
  },

  async getById(id: number) {
    const res = await api.get(`/property-bills/${id}`);
    return res.data;
  },

  async create(data: unknown) {
    const res = await api.post("/property-bills", data);
    return res.data;
  },

  async update(id: number, data: unknown) {
    const res = await api.put(`/property-bills/${id}`, data);
    return res.data;
  },

  async delete(id: number) {
    const res = await api.delete(`/property-bills/${id}`);
    return res.data;
  },

};
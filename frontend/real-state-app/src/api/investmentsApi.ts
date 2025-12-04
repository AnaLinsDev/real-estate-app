import api from "./api";

export const investmentsApi = {
  async getAll() {
    const res = await api.get("/property-investments");
    return res.data;
  },

  async getById(id: number) {
    const res = await api.get(`/property-investments/${id}`);
    return res.data;
  },

  async create(data: unknown) {
    const res = await api.post("/property-investments", data);
    return res.data;
  },

  async update(id: number, data: unknown) {
    const res = await api.put(`/property-investments/${id}`, data);
    return res.data;
  },

  async delete(id: number) {
    const res = await api.delete(`/property-investments/${id}`);
    return res.data;
  },
};

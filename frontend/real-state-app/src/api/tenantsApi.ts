import api from "./api";

export const tenantsApi = {
  async getAll() {
    const res = await api.get("/tenants");
    return res.data;
  },

  async getById(id: number) {
    const res = await api.get(`/tenants/${id}`);
    return res.data;
  },

  async create(data: unknown) {
    const res = await api.post("/tenants", data);
    return res.data;
  },

  async update(id: number, data: unknown) {
    const res = await api.put(`/tenants/${id}`, data);
    return res.data;
  },

  async delete(id: number) {
    const res = await api.delete(`/tenants/${id}`);
    return res.data;
  },
};

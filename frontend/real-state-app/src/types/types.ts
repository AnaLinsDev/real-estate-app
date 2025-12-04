export type Property = {
  id: number;
  name: string;
  type: string;
  address?: string | null;
  status: string;
  photos?: string | null; // JSON string (lista de fotos)
  notes?: string | null;
};

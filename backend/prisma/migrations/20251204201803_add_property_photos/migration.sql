-- CreateTable
CREATE TABLE "PropertyPhoto" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "property_id" INTEGER NOT NULL,
    "url_photo" TEXT NOT NULL,
    CONSTRAINT "PropertyPhoto_property_id_fkey" FOREIGN KEY ("property_id") REFERENCES "Property" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);

-- CreateIndex
CREATE INDEX "PropertyPhoto_property_id_idx" ON "PropertyPhoto"("property_id");

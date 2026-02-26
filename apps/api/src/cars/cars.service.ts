import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';
import { Prisma } from '@prisma/client';

export interface GetCarsInput {
  userId: string;
  filter_type?: string;
  sort?: string;
  limit?: number;
  offset?: number;
}

@Injectable()
export class CarsService {
  constructor(private readonly prisma: PrismaService) {}

  async getCars({ userId, filter_type, sort = 'created_at_asc', limit = 50, offset = 0 }: GetCarsInput) {
    const where: Prisma.CarWhereInput = { userId };

    if (filter_type) {
      where.type = filter_type;
    }

    // Determine sorting
    let orderBy: Prisma.CarOrderByWithRelationInput = { createdAt: 'asc' };
    if (sort === 'created_at_desc') {
      orderBy = { createdAt: 'desc' };
    }

    const [total, data] = await Promise.all([
      this.prisma.car.count({ where }),
      this.prisma.car.findMany({
        where,
        orderBy,
        skip: offset,
        take: limit,
      }),
    ]);

    return {
      data,
      meta: {
        total,
        limit,
        offset,
      },
    };
  }
}

import { Controller, Get, Query, Headers, UnauthorizedException } from '@nestjs/common';
import { CarsService } from './cars.service';

@Controller('cars')
export class CarsController {
  constructor(private readonly carsService: CarsService) {}

  @Get()
  async getCars(
    @Headers('authorization') authorization: string,
    @Query('filter_type') filter_type?: string,
    @Query('sort') sort?: string,
    @Query('limit') limitStr?: string,
    @Query('offset') offsetStr?: string,
  ) {
    if (!authorization) {
      throw new UnauthorizedException('Missing authorization token');
    }

    // In a real app, this would extract the user ID from a JWT or session
    // Since we mock it, we just assume the user is "test-user-123"
    const userId = 'test-user-123';

    // Parse int query params from express-openapi-validator output or raw strings
    const limit = limitStr ? parseInt(limitStr, 10) : 50;
    const offset = offsetStr ? parseInt(offsetStr, 10) : 0;

    return this.carsService.getCars({
      userId,
      filter_type,
      sort,
      limit,
      offset,
    });
  }
}

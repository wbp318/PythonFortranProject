module weather_calc
  implicit none

contains
  subroutine process_temperatures(temps, n, avg_temp, max_temp, min_temp)
    integer, intent(in) :: n
    real, intent(in) :: temps(n)
    real, intent(out) :: avg_temp, max_temp, min_temp
    
    avg_temp = sum(temps) / n
    max_temp = maxval(temps)
    min_temp = minval(temps)
  end subroutine process_temperatures
end module weather_calc